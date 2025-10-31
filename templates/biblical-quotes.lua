-- Filtr Lua dla pandoc - formatowanie cytatów biblijnych
-- Automatycznie formatuje cytaty w kursywie jako cytaty biblijne

function Emph(elem)
    -- Sprawdź czy tekst wygląda jak cytat biblijny
    local text = pandoc.utils.stringify(elem)

    -- Wzorce dla odniesień biblijnych
    local patterns = {
        "%(Łk %d+[,:][%d%-]+%)",     -- (Łk 23,34)
        "%(Mt %d+[,:][%d%-]+%)",     -- (Mt 26,28)
        "%(Mk %d+[,:][%d%-]+%)",     -- (Mk 14,36)
        "%(J %d+[,:][%d%-]+%)",      -- (J 11,50)
        "%(Rz %d+[,:][%d%-]+%)",     -- (Rz 3,23)
        "%(1 Kor %d+[,:][%d%-]+%)",  -- (1 Kor 11,26)
        "%([A-Za-ząćęłńóśźż]+ %d+[,:][%d%-]+%)" -- Ogólny wzorzec
    }

    -- Sprawdź czy tekst zawiera odniesienie biblijne
    local is_biblical = false
    for _, pattern in ipairs(patterns) do
        if string.match(text, pattern) then
            is_biblical = true
            break
        end
    end

    -- Sprawdź też czy to cytat (zaczyna się od „ lub " lub zawiera charakterystyczne słowa)
    if string.match(text, "^[„\"]") or
       string.match(text, "Ojcze") or
       string.match(text, "Panie") or
       string.match(text, "przebacz") or
       string.match(text, "błogosławieni") then
        is_biblical = true
    end

    -- Jeśli to cytat biblijny, opakuj w specjalne formatowanie
    if is_biblical then
        return pandoc.RawInline('latex', '\\bq{' .. text .. '}')
    else
        return elem
    end
end

-- Formatowanie sekcji z numeracją rzymską
function Header(elem)
    if elem.level == 2 then
        -- Dodaj ozdobnik przed ważnymi sekcjami
        local ornament = pandoc.RawBlock('latex', '\\sectionbreak')
        return {ornament, elem}
    end
    return elem
end

-- Formatowanie pierwszego akapitu każdej sekcji z ozdobnym inicjałem
local first_para_after_header = false

function Block(elem)
    if elem.t == "Header" then
        first_para_after_header = true
        return elem
    elseif elem.t == "Para" and first_para_after_header then
        first_para_after_header = false

        -- Pobierz pierwszy znak akapitu
        if elem.content and #elem.content > 0 then
            local first = elem.content[1]
            if first.t == "Str" then
                local text = first.text
                if #text > 0 then
                    local first_char = text:sub(1, 1)
                    local rest = text:sub(2)

                    -- Utwórz ozdobny inicjał
                    local lettrine = pandoc.RawInline('latex',
                        '\\lettrine[lines=2]{' .. first_char .. '}{')

                    -- Pierwsze słowo małymi kapitalikami
                    local words = {}
                    local first_word_end = rest:find(" ") or #rest
                    local first_word = rest:sub(1, first_word_end - 1)
                    local rest_text = rest:sub(first_word_end)

                    local small_caps = pandoc.RawInline('latex',
                        '\\textsc{' .. first_word:lower() .. '}')
                    local close = pandoc.RawInline('latex', '}')

                    -- Zbuduj nową zawartość
                    local new_content = {lettrine, small_caps, close}
                    if #rest_text > 0 then
                        table.insert(new_content, pandoc.Str(rest_text))
                    end

                    -- Dodaj resztę zawartości
                    for i = 2, #elem.content do
                        table.insert(new_content, elem.content[i])
                    end

                    elem.content = new_content
                end
            end
        end
    end
    return elem
end

-- Zwróć filtry w odpowiedniej kolejności
return {
    {Emph = Emph},
    {Header = Header},
    {Block = Block}
}